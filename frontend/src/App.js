import React, { useState } from "react";
import "./App.css";
import Dropdown from "./Dropdown";

const App = () => {
  const [summary, setSummary] = useState("");
  const [isLoading, setIsLoading] = useState(false); // Loading state for user feedback

  // Fetch the summary when a champion is selected
  const fetchSummary = async (championName) => {
    if (!championName) {
      setSummary("Please select a champion.");
      return;
    }

    setIsLoading(true); // Start loading
    setSummary(""); // Clear previous summary

    try {
      const response = await fetch("http://localhost:5000/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ champion_name: championName }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();
      setSummary(data.summary || "No summary available for this champion."); // Fallback message
    } catch (error) {
      console.error("Error fetching summary:", error);
      setSummary("Error generating summary. Please try again.");
    } finally {
      setIsLoading(false); // Stop loading
    }
  };

  const backgroundStyle = {
    backgroundImage: `url('/assets/background.jpeg')`, // Replace with your image path
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    minHeight: "100vh", // Minimum height for better responsiveness
    width: "100%", // Full width
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: "20px",
    boxSizing: "border-box",
  };

  return (
    <div className="App" style={backgroundStyle}>
      {/* App Title */}
      <h1 className="app-title">League of Legends Summarizer</h1>

      {/* Dropdown Component */}
      <Dropdown onChampionSelect={fetchSummary} />

      {/* Summary Section */}
      <div className="summary-container">
        <h2 className="summary-title">Summary</h2>
        {isLoading ? (
          <p>Loading...</p> // Display loading state
        ) : (
          <p>{summary || "Select a champion to view their summary."}</p>
        )}
      </div>
    </div>
  );
};

export default App;
