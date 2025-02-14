import React, { useState, useEffect } from "react";
import axios from "axios";

const Dashboard = () => {
  const [pendingUsers, setPendingUsers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/get_pending_users/")
      .then(res => setPendingUsers(res.data.pending_users))
      .catch(err => console.log(err));
  }, []);

  const sendNotifications = () => {
    axios.post("http://127.0.0.1:8000/send_notifications/")
      .then(() => alert("Notifications Sent!"))
      .catch(err => console.log(err));
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Google Form Submissions</h1>
      <table className="border-collapse border border-gray-300 w-full mt-4">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">Email</th>
            <th className="border p-2">Status</th>
          </tr>
        </thead>
        <tbody>
          {pendingUsers.map((email, index) => (
            <tr key={index}>
              <td className="border p-2">{email}</td>
              <td className="border p-2 text-red-500">Pending</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button 
        className="bg-blue-500 text-white px-4 py-2 rounded mt-4"
        onClick={sendNotifications}
      >
        Send WhatsApp Notifications
      </button>
    </div>
  );
};

export default Dashboard;
