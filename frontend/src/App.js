import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {

  const [page, setPage] = useState("login");

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [otp, setOtp] = useState("");

  const [error, setError] = useState("");
  const [timer, setTimer] = useState(60);


  useEffect(() => {
    if (page === "otp" && timer > 0) {
      const interval = setInterval(() => {
        setTimer(timer - 1);
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [timer, page]);


  const registerUser = async () => {
    setError("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/register/", {
        username,
        email,
        password
      });

      alert(res.data.message);
      setPage("login");

    } catch (err) {
      if (err.response?.data) {
        const data = err.response.data;
        if (data.username) setError(data.username[0]);
        else if (data.email) setError(data.email[0]);
        else if (data.password) setError(data.password[0]);
        else setError("Registration failed");
      }
    }
  };


  const loginUser = async () => {
    setError("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/login/", {
        username,
        password
      });

      alert(res.data.message);
      setPage("otp");
      setTimer(60);

    } catch (err) {
      setError(err.response?.data?.error || "Login failed");
    }
  };


  const resendOtp = async () => {
    try {

      const res = await axios.post("http://127.0.0.1:8000/api/login/", {
        username,
        password
      });

      alert("OTP resent");
      setTimer(60);

    } catch {
      alert("Failed to resend OTP");
    }
  };


  const verifyOtp = async () => {
    try {

      const res = await axios.post("http://127.0.0.1:8000/api/verify-otp/", {
        username,
        otp
      });

      alert(res.data.message);
      setPage("welcome");

    } catch (err) {
      setError(err.response?.data?.error || "OTP failed");
    }
  };


  const logout = () => {
    setPage("login");
  };


  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">

      <div className="bg-white p-8 rounded-lg shadow-lg w-96">

        <h1 className="text-2xl font-bold text-center mb-6">
          OTP Authentication
        </h1>

        {error && (
          <p className="text-red-500 text-center mb-3">{error}</p>
        )}


        {page === "register" && (
          <>
            <input
              className="w-full p-2 border rounded mb-3"
              placeholder="Username"
              onChange={(e) => setUsername(e.target.value)}
            />

            <input
              className="w-full p-2 border rounded mb-3"
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
            />

            <input
              type="password"
              className="w-full p-2 border rounded mb-3"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />

            <button
              className="w-full bg-blue-500 text-white p-2 rounded"
              onClick={registerUser}
            >
              Register
            </button>

            <p
              className="text-center mt-3 text-blue-500 cursor-pointer"
              onClick={() => setPage("login")}
            >
              Already have account? Login
            </p>
          </>
        )}


        {page === "login" && (
          <>
            <input
              className="w-full p-2 border rounded mb-3"
              placeholder="Username"
              onChange={(e) => setUsername(e.target.value)}
            />

            <input
              type="password"
              className="w-full p-2 border rounded mb-3"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />

            <button
              className="w-full bg-green-500 text-white p-2 rounded"
              onClick={loginUser}
            >
              Login
            </button>

            <p
              className="text-center mt-3 text-blue-500 cursor-pointer"
              onClick={() => setPage("register")}
            >
              Create account
            </p>
          </>
        )}


        {page === "otp" && (
          <>
            <input
              className="w-full p-2 border rounded mb-3"
              placeholder="Enter OTP"
              onChange={(e) => setOtp(e.target.value)}
            />

            <button
              className="w-full bg-purple-500 text-white p-2 rounded"
              onClick={verifyOtp}
            >
              Verify OTP
            </button>

            <p className="text-center mt-3 text-gray-500">
              Time remaining: {timer}s
            </p>

            {timer === 0 && (
              <button
                className="w-full mt-2 bg-orange-500 text-white p-2 rounded"
                onClick={resendOtp}
              >
                Resend OTP
              </button>
            )}
          </>
        )}


        {page === "welcome" && (
          <>
            <h2 className="text-center text-xl font-bold mb-4">
              Welcome {username} 🎉
            </h2>

            <button
              className="w-full bg-red-500 text-white p-2 rounded"
              onClick={logout}
            >
              Logout
            </button>
          </>
        )}

      </div>
    </div>
  );
}

export default App;