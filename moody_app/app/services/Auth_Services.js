import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Toast } from "@ant-design/react-native";

// Define your base URL for API requests (replace with your actual API endpoint)
const API_URL = "http://127.0.0.1:8000";

export const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}/auth/login/`, {
      email,
      password
    });
    const { token } = response.data;
    console.log(response);
    // Store the token securely using AsyncStorage or a more secure solution
    await AsyncStorage.setItem("userToken", token);
    return token;
  } catch (error) {
    // Toast.fail("Fail");

    console.error("Login Error: ", error.response || error.message);
    throw new Error("Login failed");
  }
};

export const logout = async () => {
  try {
    await AsyncStorage.removeItem("userToken");
  } catch (error) {
    console.error("Logout Error: ", error);
  }
};

export const checkAuth = async () => {
  try {
    const token = await AsyncStorage.getItem("userToken");
    return token != null;
  } catch (error) {
    console.error("Error checking auth: ", error);
    return false;
  }
};
