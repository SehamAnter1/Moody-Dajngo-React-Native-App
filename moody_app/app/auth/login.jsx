import React, {useState} from "react";
import {View, Text, TextInput, Button} from "react-native";
import {useRouter} from "expo-router";
import AuthLayout from "./index";
import {useAuth} from "../context/Auth_Context";

const Login = () => {
    const router = useRouter();
    const {loginUser, isAuthenticated, loading} = useAuth();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        await loginUser(email, password);
        if (isAuthenticated) {
            router.push("/");
        }
    };
    return (
        <AuthLayout title="login">
            <View>
                <Text>Login</Text>
                <TextInput placeholder="Email" value={email} onChangeText={setEmail} />
                <TextInput placeholder="Password" secureTextEntry value={password} onChangeText={setPassword} />
                <Button title="login" onPress={handleLogin} />
            </View>
        </AuthLayout>
    );
};

export default Login;
