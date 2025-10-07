
import React, { useState } from 'react';
import Schedule from './Schedule';
import './App.css';  // Add basic styles

function App() {
 const [userId, setUser_Id] = useState(null);
const [step, setStep] = useState('setup'); // 'setup', 'add-subjects', 'schedule'  // 'setup', 'add-subjects', 'schedule'

  const handleSetup = async (userData) => {
    try {
      const response = await createUser (userData);
      setUser_Id(response.data.id);
      setStep('add-subjects');
    } catch (error) {
      console.error('Setup error:', error);
    }
  };

  if (step === 'setup') {
    return (
      <div className="setup">
        <h1>Smart Study Scheduler Setup</h1>
        <form onSubmit={(e) => { e.preventDefault(); handleSetup({ name: e.target.name.value, energy_peak: e.target.peak.value, user_type: e.target.type.value }); }}>
          <input name="name" placeholder="Your Name" required />
          <select name="peak">
            <option value="morning">Morning Peak</option>
            <option value="evening">Evening Peak</option>
          </select>
          <select name="type">
            <option value="morning_person">Morning Person</option>
            <option value="night_owl">Night Owl</option>
          </select>
          <button type="submit">Create Profile</button>
        </form>
      </div>
    );
  }

  return <Schedule userId={userId} setStep={setStep} />;
}

export default App;
