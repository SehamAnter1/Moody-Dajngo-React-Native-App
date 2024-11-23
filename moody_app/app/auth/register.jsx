import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { useRouter } from 'expo-router';

const RegisterScreen = () => {
  const router = useRouter();

  const handleRegister = () => {
    // After successful registration, navigate to login page or home page
    router.push('/auth/login');
  };

  return (
    <View>
      <Text>Register</Text>
      <TextInput placeholder="Email" />
      <TextInput placeholder="Password" secureTextEntry />
      <Button title="Register" onPress={handleRegister} />
    </View>
  );
};

export default RegisterScreen;
