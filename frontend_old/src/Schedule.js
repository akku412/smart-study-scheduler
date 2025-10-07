
import React, { useState, useEffect } from 'react';
import { getSchedule, addSubject, markComplete, reschedule } from './api';

function Schedule({ userId, setStep }) {
  const [schedule, setSchedule] = useState([]);
  const [newSubject, setNewSubject] = useState({ name: '', difficulty: 5, exam_date: '' });
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (userId) fetchSchedule();
  }, [userId]);

  const fetchSchedule = async () => {
    try {
      const response = await getSchedule(userId);
      setSchedule(response.data.schedule || []);
    } catch (error) {
      console.error('Schedule fetch error:', error);
    }
  };

  const handleAddSubject = async (e) => {
    e.preventDefault();
    try {
      await addSubject(userId, newSubject);
      setNewSubject({ name: '', difficulty: 5, exam_date: '' });
      fetchSchedule();  // Regenerate schedule
      setMessage('Subject added! Schedule updated.');
    } catch (error) {
      console.error('Add subject error:', error);
    }
  };

  const handleComplete = async (scheduleItem, completed) => {
    // Note: For demo, we simulate schedule_id as index; in full app, store IDs
    await markComplete(scheduleItem.id || schedule.indexOf(scheduleItem) + 1, completed);
    fetchSchedule();
    setMessage(completed ? 'Great job completing that session!' : 'Marked as missed—rescheduling soon.');
  };

  const handleReschedule = async () => {
    try {
      const response = await reschedule(userId);
      setSchedule(response.data.new_slots.flat() || []);
      setMessage(response.data.message);
    } catch (error) {
      console.error('Reschedule error:', error);
    }
  };

  return (
    <div className="dashboard">
      <h1>Your AI-Generated Schedule</h1>
      <button onClick={() => setStep('setup')}>Back to Setup</button>
      
      {message && <p className="message">{message}</p>}
      
      {/* Add Subject Form */}
      <section>
        <h2>Add a Subject</h2>
        <form onSubmit={handleAddSubject}>
          <input
            type="text"
            placeholder="Subject Name (e.g., Data Structures)"
            value={newSubject.name}
            onChange={(e) => setNewSubject({ ...newSubject, name: e.target.value })}
            required
          />
          <input
            type="number"
            min="1"
            max="10"
            placeholder="Difficulty (1-10)"
            value={newSubject.difficulty}
            onChange={(e) => setNewSubject({ ...newSubject, difficulty: parseFloat(e.target.value) })}
            required
          />
          <input
            type="date"
            value={newSubject.exam_date}
            onChange={(e) => setNewSubject({ ...newSubject, exam_date: e.target.value })}
            required
          />
          <button type="submit">Add Subject & Update Schedule</button>
        </form>
      </section>

      {/* Schedule Display */}
      <section>
        <h2>Weekly Schedule</h2>
        <button onClick={handleReschedule}>Reschedule Missed Sessions</button>
        {schedule.length === 0 ? (
          <p>No schedule yet—add subjects to generate one!</p>
        ) : (
          <ul>
            {schedule.map((item, index) => (
              <li key={index} className="schedule-item">
                <strong>{item.subject}</strong> - {item.type} session<br />
                Start: {new Date(item.start).toLocaleString()}<br />
                Duration: {item.duration} minutes<br />
                <button onClick={() => handleComplete(item, true)}>Mark Complete</button>
                <button onClick={() => handleComplete(item, false)}>Mark Missed</button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}

export default Schedule;
