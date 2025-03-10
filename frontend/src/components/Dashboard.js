import React, { useState } from "react";
import axios from "axios";
import { auth } from "../firebase";
import { signOut } from "firebase/auth";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const [inputText, setInputText] = useState("");
  const [generatedEmail, setGeneratedEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await signOut(auth);
      navigate("/login");
    } catch (err) {
      console.error("Logout failed:", err);
    }
  };

  const generateEmail = async () => {
    if (!inputText.trim()) {
      alert("Please enter some text before generating the email.");
      return;
    }

    setLoading(true);
    const endpoint = "http://127.0.0.1:5000/search"; // Replace with your Flask API endpoint

    try {
      const response = await axios.post(
        endpoint,
        {
          query: inputText,
        },
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      // Adjust based on the actual API response structure.
      const generatedText = response.data.output;
      setGeneratedEmail(generatedText);
      setHistory((prev) => [
        ...prev,
        { input: inputText, email: generatedText },
      ]);
    } catch (error) {
      console.error("Error generating email:", error);
      setGeneratedEmail("Failed to generate email. Please try again.");
    }
    setLoading(false);
  };

  const copyToClipboard = () => {
    if (generatedEmail) {
      navigator.clipboard
        .writeText(generatedEmail)
        .then(() => alert("Email copied to clipboard!"))
        .catch(() => alert("Failed to copy email."));
    }
  };

  const clearFields = () => {
    setInputText("");
    setGeneratedEmail("");
  };

  const downloadEmail = () => {
    if (generatedEmail) {
      const element = document.createElement("a");
      const file = new Blob([generatedEmail], { type: "text/plain" });
      element.href = URL.createObjectURL(file);
      element.download = "generated_email.txt";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    }
  };

  const redirectToMail = async () => {
    if (generatedEmail) {
      const endpoint = "http://127.0.0.1:5000/open"; // Replace with your Flask API endpoint for redirect
  
      try {
        const response = await axios.post(
          endpoint,
          {
            to: "dummy@gmail.com",
            body:inputText,
            type:"mail"
          },
          {
            headers: { "Content-Type": "application/json" },
          }
        );
  
        // Assuming the endpoint returns a URL to redirect to
        const redirectUrl = response.data.url;
        window.location.href = redirectUrl;
      } catch (error) {
        console.error("Error redirecting to mail:", error);
        alert("Failed to redirect to mail. Please try again.");
      }
    }
  };

  return (
    <div className="dashboard-container">
      <div className="header">
        <h2>Email Generator Dashboard</h2>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>
      <textarea
        rows="4"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter your prompt or text here..."
      />
      <div className="button-group">
        <button onClick={generateEmail} disabled={loading}>
          {loading ? "Generating..." : "Generate Email"}
        </button>
        <button onClick={copyToClipboard} disabled={!generatedEmail}>
          Copy Email
        </button>
        <button onClick={downloadEmail} disabled={!generatedEmail}>
          Download Email
        </button>
        <button onClick={clearFields}>Clear</button>
        <button onClick={redirectToMail} disabled={!generatedEmail}>
          Redirect to Mail
        </button>
      </div>
      <h3>Generated Email:</h3>
      <div className="generated-email">
        {generatedEmail || "Your generated email will appear here..."}
      </div>
      {history.length > 0 && (
        <div className="history">
          <h3>History</h3>
          {history.map((item, index) => (
            <div key={index} className="history-item">
              <p>
                <strong>Prompt:</strong> {item.input}
              </p>
              <p>
                <strong>Email:</strong> {item.email}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}