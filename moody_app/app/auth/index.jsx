import React from "react";
import {View, Text, StyleSheet} from "react-native";
export default function AuthLayout({children}) {
    return (
        <View style={styles.container}>
            <View style={styles.header}>
                <Text style={styles.title}>My App</Text>
            </View>
            <View style={styles.body}>{children}</View>
        </View>
    );
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        padding: 20,
        backgroundColor: "#fff",
    },
    header: {
        marginBottom: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
    },
    body: {
        width: "100%",
        maxWidth: 400,
        marginTop: 20,
    },
});
