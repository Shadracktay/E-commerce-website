import React from "react";
import { View, Text, SafeAreaView, FlatList, TouchableOpacity } from "react-native";
import { Card } from "@/components/ui/card";

const products = [
  { id: "1", name: "Laptop", price: "GH₵2500", seller: "John Doe" },
  { id: "2", name: "Smartphone", price: "GH₵1200", seller: "Jane Doe" },
  { id: "3", name: "Headphones", price: "GH₵300", seller: "Mark Smith" },
];

const ProductItem = ({ item }) => (
  <Card className="p-4 m-2 border rounded-lg">
    <Text className="text-lg font-bold">{item.name}</Text>
    <Text className="text-gray-600">Price: {item.price}</Text>
    <Text className="text-gray-600">Seller: {item.seller}</Text>
    <TouchableOpacity className="mt-2 p-2 bg-blue-500 rounded-lg">
      <Text className="text-white text-center">Order Now</Text>
    </TouchableOpacity>
  </Card>
);

const App = () => {
  return (
    <SafeAreaView className="flex-1 p-4 bg-gray-100">
      <View className="flex-row justify-between items-center mb-4 px-4">
        <Text className="text-2xl font-bold">Welcome to DASA App</Text>
        <TouchableOpacity className="px-4 py-2 bg-green-600 rounded-lg shadow-md">
          <Text className="text-white font-semibold">Sign In</Text>
        </TouchableOpacity>
      </View>
      <FlatList
        data={products}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => <ProductItem item={item} />}
      />
    </SafeAreaView>
  );
};

export default App;
