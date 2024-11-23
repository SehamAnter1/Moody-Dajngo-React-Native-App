// /context/AuthContext.js

import React, { createContext, useContext, useState, useEffect } from 'react';
import { login, logout, checkAuth } from '../services/Auth_Services';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuthenticationStatus = async () => {
      const authStatus = await checkAuth();
      setIsAuthenticated(authStatus);
      setLoading(false);
    };

    checkAuthenticationStatus();
  }, []);

  const loginUser = async (email, password) => {
    try {
      await login(email, password);
      setIsAuthenticated(true);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const logoutUser = async () => {
    await logout();
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, loading, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};
