import type { Product } from '../data/products';

const API_BASE_URL = 'http://localhost:8000/api';

export async function fetchProducts(): Promise<Product[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/products`);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error("Error fetching products from backend:", error);
    return [];
  }
}

export async function getRecommendations(userPreference: string): Promise<{
  products: Product[];
  filters: Record<string, unknown>;
}> {
  try {
    const response = await fetch(`${API_BASE_URL}/recommendations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: userPreference }),
    });

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();
    return { products: data.products, filters: data.filters };
  } catch (error) {
    console.error("Error fetching AI recommendations from backend:", error);
    return { products: [], filters: {} };
  }
}
