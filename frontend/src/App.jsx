import './App.css'
import React, { useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  Cell,
} from "recharts";
import "./App.css";

function App() {
  const [videoUrl, setVideoUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedSentiment, setSelectedSentiment] = useState(null);

  const handleAnalyze = async () => {
    if (!videoUrl) return;
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/analyze", {
        url: videoUrl,
      });
      setResult(response.data);
      setSelectedSentiment(null); // Reset seleksi ketika hasil baru datang
    } catch (error) {
      console.error("Gagal menganalisis:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleBarClick = (data) => {
    const sentimentName = data.name;
    setSelectedSentiment((prev) =>
      prev === sentimentName ? null : sentimentName
    );
  };

  const chartData = result
    ? Object.entries(result).map(([sentimen, data]) => ({
        name: sentimen,
        jumlah: data.jumlah,
      }))
    : [];

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>Analisis Sentimen Komentar YouTube</h1>

      <input
        type="text"
        placeholder="Tempel URL video YouTube di sini..."
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
        style={{ width: "60%", padding: "0.5rem", marginRight: "1rem" }}
      />
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Memproses..." : "Analisis"}
      </button>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h2>Hasil Analisis</h2>

          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={chartData} onClick={(e) => handleBarClick(e.activePayload?.[0]?.payload)}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis allowDecimals={false} />
              <Tooltip />
              <Bar dataKey="jumlah" fill="#8884d8">
                {chartData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={
                      entry.name === selectedSentiment ? "#82ca9d" : "#8884d8"
                    }
                  />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>

          {selectedSentiment && (
            <div style={{ marginTop: "2rem" }}>
              <h3>Contoh Komentar ({selectedSentiment})</h3>
              <table border="1" cellPadding="8" cellSpacing="0" width="100%">
                <thead>
                  <tr>
                    <th>No</th>
                    <th>Komentar</th>
                  </tr>
                </thead>
                <tbody>
                  {result[selectedSentiment]?.komentar.map((komentar, i) => (
                    <tr key={`${selectedSentiment}-${i}`}>
                      <td>{i + 1}</td>
                      <td>{komentar}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
