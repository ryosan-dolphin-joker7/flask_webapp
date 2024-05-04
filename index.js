// pages/index.js

import React, { useState, useEffect } from "react";
import axios from "axios";

const Index = () => {
  const [data, setData] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get("/api/data");
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <h1>Frontend with Next.js</h1>
      <p>Data from Flask backend: {data}</p>
    </div>
  );
};

export default Index;
