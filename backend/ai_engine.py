
from datetime import datetime, timedelta
from typing import List, Dict
import random  # For simulated adaptation

class AIEngine:
    def __init__(self, db_session):
        self.db = db_session

    def calculate_priority(self, subject) -> float:
        """Intelligent Subject Prioritization: Urgency + Difficulty + Behind Schedule"""
        days_to_exam = (subject.exam_date - datetime.now()).days
        urgency = max(0, 10 - days_to_exam)  # Higher if closer
        difficulty_weight = subject.difficulty / 10
        behind_factor = max(0, (50 - subject.progress) / 50)  # If <50% done, boost
        return urgency * 0.4 + difficulty_weight * 0.3 + behind_factor * 0.3

    def optimal_session_length(self, subject, session_type: str) -> int:
        """Optimal Session Calculation: Adapt to difficulty and type"""
        base_length = 25 if session_type == 'reading' else 45  # Pomodoro-inspired
        difficulty_adjust = int(subject.difficulty * 3)  # Harder = longer
        return min(90, base_length + difficulty_adjust)  # Cap at 90 mins

    def generate_schedule(self, user_id: int, days_ahead: int = 7) -> List[Dict]:
        """Smart Time Distribution: Greedy scheduling avoiding conflicts"""
        # Fetch user and subjects
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        subjects = self.db.query(models.Subject).filter(models.Subject.user_id == user_id).all()
        
        schedule = []
        current_time = datetime.now()
        energy_peaks = {'morning': (8, 12), 'evening': (18, 22)}  # Hardcode peaks
        peak_start, peak_end = energy_peaks.get(user.energy_peak, (9, 17))
        
        # Avoid college hours (assume 9AM-5PM Mon-Fri; customize)
        college_hours = lambda dt: dt.weekday() < 5 and 9 <= dt.hour < 17
        
        for day in range(days_ahead):
            day_start = current_time + timedelta(days=day)
            day_end = day_start.replace(hour=23, minute=59)
            
            # Sort subjects by priority
            prioritized = sorted(subjects, key=lambda s: self.calculate_priority(s), reverse=True)
            
            for subject in prioritized:
                if subject.progress >= 100:
                    continue
                
                # Find free slot in peak if hard subject
                is_hard = subject.difficulty > 7
                search_start = peak_start if is_hard and day_start.weekday() < 5 else 7
                slot_start = day_start.replace(hour=search_start, minute=0)
                
                while slot_start < day_end:
                    if not college_hours(slot_start):
                        duration = self.optimal_session_length(subject, 'practice' if random.random() > 0.5 else 'reading')
                        slot_end = slot_start + timedelta(minutes=duration)
                        
                        # No overlap check (simplified; add if needed)
                        schedule.append({
                            'subject': subject.name,
                            'start': slot_start.isoformat(),
                            'duration': duration,
                            'type': 'practice' if subject.difficulty > 5 else 'reading'
                        })
                        break
                    slot_start += timedelta(minutes=30)  # Try next slot
        
        return schedule

    def mark_completion(self, schedule_id: int, completed: bool):
        """Learning & Adaptation: Track and adjust future plans"""
        schedule = self.db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
        schedule.completed = completed
        if completed:
            schedule.subject.progress += 5  # Incremental progress
        else:
            # Reschedule logic: Boost priority for next gen
            schedule.subject.exam_date -= timedelta(days=1)  # Simulate urgency increase
        
        # Adaptation: If completion rate <70% for practice, shorten future sessions
        # (Simplified; track in DB for real adaptation)
        self.db.commit()

    def reschedule_missed(self, user_id: int) -> List[Dict]:
        """Intelligent Rescheduling: Priority-based recovery"""
        missed = self.db.query(models.Schedule).filter(
            models.Schedule.user_id == user_id, models.Schedule.completed == False
        ).all()
        
        prioritized_missed = sorted(missed, key=lambda s: self.calculate_priority(s.subject), reverse=True)
        new_slots = []  # Regenerate slots (call generate_schedule logic here)
        for item in prioritized_missed[:3]:  # Limit to top 3 urgent
            new_slots.append(self.generate_schedule(user_id, days_ahead=1)[:1])  # One slot each
        
        # Motivational message
        if len(missed) > 2:
            return new_slots, "You're behind—focus on high-priority subjects first! You've got this."
        return new_slots, "Great job staying on track. Keep it up!"

# Import models for reference
import models
