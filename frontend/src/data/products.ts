export interface Product {
  id: string;
  name: string;
  price: number;
  category: string;
  description: string;
  imageUrl: string;
}

export const products: Product[] = [
  {
    id: "p1",
    name: "Quantum X Pro Smartphone",
    price: 899,
    category: "Phones",
    description: "Latest 5G smartphone with a stunning OLED display and advanced computational photography features.",
    imageUrl: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p2",
    name: "Nebula Lite Phone",
    price: 349,
    category: "Phones",
    description: "Affordable smartphone with great battery life and a reliable camera for everyday use.",
    imageUrl: "https://images.unsplash.com/photo-1598327105666-5b89351cb31b?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p3",
    name: "Aura Noise-Canceling Headphones",
    price: 249,
    category: "Audio",
    description: "Premium over-ear headphones with active noise cancellation and 30-hour battery life.",
    imageUrl: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p4",
    name: "Zenith Ultrabook 14",
    price: 1199,
    category: "Laptops",
    description: "Sleek and powerful ultrabook perfect for professionals on the go. Features an M2 equivalent chip.",
    imageUrl: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p5",
    name: "Atlas Smartwatch Series 5",
    price: 199,
    category: "Wearables",
    description: "Fitness and health tracking smartwatch with built-in GPS and heart rate monitoring.",
    imageUrl: "https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p6",
    name: "Echo Portable Bluetooth Speaker",
    price: 59,
    category: "Audio",
    description: "Compact waterproof speaker with surprisingly loud and clear sound.",
    imageUrl: "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p7",
    name: "Nova 4K Action Camera",
    price: 149,
    category: "Cameras",
    description: "Capture your adventures in stunning 4K resolution. Waterproof up to 30 meters.",
    imageUrl: "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=600&auto=format&fit=crop"
  },
  {
    id: "p8",
    name: "Lumina Desk Lamp with Wireless Charging",
    price: 45,
    category: "Accessories",
    description: "Modern LED desk lamp with adjustable brightness and a built-in wireless charging pad.",
    imageUrl: "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?q=80&w=600&auto=format&fit=crop"
  }
];
