
import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const createUser  = (userData) => axios.post(`${API_BASE}/users/`, userData);
export const addSubject = (userId, subjectData) => axios.post(`${API_BASE}/subjects/${userId}`, subjectData);
export const getSchedule = (userId) => axios.get(`${API_BASE}/schedule/${userId}`);
export const markComplete = (scheduleId, completed) => axios.post(`${API_BASE}/complete/${scheduleId}`, { completed });
export const reschedule = (userId) => axios.get(`${API_BASE}/reschedule/${userId}`);
