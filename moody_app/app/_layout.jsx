import {DarkTheme, DefaultTheme, ThemeProvider} from "@react-navigation/native";
import {useFonts} from "expo-font";
import {Stack} from "expo-router";
import * as SplashScreen from "expo-splash-screen";
import {useState} from "react";
import "react-native-reanimated";

import {useColorScheme} from "@/hooks/useColorScheme";
import AsyncStorage from "@react-native-async-storage/async-storage";
import {AuthProvider, useAuth} from "./context/Auth_Context";

export default function RootLayout() {
    const colorScheme = useColorScheme();
    const [loaded] = useFonts({
        SpaceMono: require("../assets/fonts/SpaceMono-Regular.ttf"),
    });

    // Wrap your whole layout with the AuthProvider to ensure useAuth works
    return (
        <AuthProvider>
            <RootLayoutWithAuth colorScheme={colorScheme} />
        </AuthProvider>
    );
}

function RootLayoutWithAuth({colorScheme}) {
    const {isAuthenticated, loading} = useAuth();

    // if (loading) {
    //    r // Show a loading state until authentication status is loaded
    //     return null; // You can replace with a loading spinner or splash screen
    // }
    console.log(isAuthenticated);
    return (
        <ThemeProvider value={colorScheme === "dark" ? DarkTheme : DefaultTheme}>
            <Stack>
                {isAuthenticated ? (
                    <Stack.Screen name="(tabs)" options={{headerShown: false}} />
                ) : (
                    <Stack.Screen name="auth/login" options={{headerShown: false}} />
                )}
                <Stack.Screen name="+not-found" />
            </Stack>
        </ThemeProvider>
    );
}
