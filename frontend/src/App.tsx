import React, { useState, useEffect } from 'react';
import { Search, Sparkles, Loader2, Tag, DollarSign, Cpu } from 'lucide-react';
import type { Product } from './data/products';
import { fetchProducts, getRecommendations } from './services/ai';
import './App.css';

interface GeminiFilters {
  category?: string | null;
  max_price?: number | null;
  brand?: string | null;
  feature?: string | null;
}

function App() {
  const [query, setQuery] = useState('');
  const [allProducts, setAllProducts] = useState<Product[]>([]);
  const [displayedProducts, setDisplayedProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [extractedFilters, setExtractedFilters] = useState<GeminiFilters | null>(null);

  useEffect(() => {
    const loadProducts = async () => {
      const data = await fetchProducts();
      setAllProducts(data);
      setDisplayedProducts(data);
    };
    loadProducts();
  }, []);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) {
      setDisplayedProducts(allProducts);
      setExtractedFilters(null);
      setHasSearched(false);
      return;
    }

    setIsLoading(true);
    setHasSearched(true);
    setExtractedFilters(null);

    try {
      const { products, filters } = await getRecommendations(query);
      setDisplayedProducts(products);
      setExtractedFilters(filters as GeminiFilters);
    } catch (error) {
      console.error("Failed to get recommendations", error);
      setDisplayedProducts(allProducts);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setQuery('');
    setDisplayedProducts(allProducts);
    setExtractedFilters(null);
    setHasSearched(false);
  };

  const activeFilters = extractedFilters
    ? Object.entries(extractedFilters).filter(([, v]) => v !== null && v !== undefined)
    : [];

  return (
    <div className="app-container">
      <header className="header">
        <div className="header-content">
          <div className="logo">
            <Sparkles className="logo-icon" />
            <h1>AI Recommender</h1>
          </div>
          <p className="subtitle">Describe what you need — Gemini AI extracts your intent, MongoDB finds the match.</p>
        </div>
      </header>

      <main className="main-content">
        <div className="search-section">
          <form onSubmit={handleSearch} className="search-form">
            <div className="search-input-wrapper">
              <Search className="search-icon" />
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder='e.g., "I want a phone under $500 with a good camera"'
                className="search-input"
              />
              {query && (
                <button type="button" onClick={handleReset} className="clear-btn">
                  Clear
                </button>
              )}
            </div>
            <button type="submit" className="submit-btn" disabled={isLoading}>
              {isLoading ? (
                <>
                  <Loader2 className="spinner" />
                  Thinking...
                </>
              ) : (
                'Find Products'
              )}
            </button>
          </form>

          {/* Gemini Extracted Filters */}
          {activeFilters.length > 0 && (
            <div className="filters-bar">
              <span className="filters-label">
                <Cpu size={14} />
                Gemini understood:
              </span>
              {activeFilters.map(([key, value]) => (
                <span key={key} className={`filter-pill filter-pill--${key}`}>
                  {key === 'max_price' ? (
                    <><DollarSign size={12} /> Budget: up to ${value}</>
                  ) : key === 'category' ? (
                    <><Tag size={12} /> Category: {String(value)}</>
                  ) : (
                    <>{key}: {String(value)}</>
                  )}
                </span>
              ))}
            </div>
          )}
        </div>

        <div className="results-section">
          <div className="results-header">
            <h2>{hasSearched ? 'Recommended for you' : 'All Products'}</h2>
            <span className="results-count">{displayedProducts.length} items found</span>
          </div>

          {isLoading ? (
            <div className="loading-state">
              <p className="loading-text">
                <Loader2 className="spinner-inline" size={16} />
                Gemini is analyzing your query &amp; querying MongoDB...
              </p>
              <div className="skeleton-grid">
                {[1, 2, 3, 4].map(n => (
                  <div key={n} className="skeleton-card"></div>
                ))}
              </div>
            </div>
          ) : displayedProducts.length > 0 ? (
            <div className="product-grid">
              {displayedProducts.map(product => (
                <div key={product.id} className="product-card">
                  <div className="product-info">
                    <div className="product-header-inline">
                      <h3 className="product-name">{product.name}</h3>
                      <span className="product-category">{product.category}</span>
                    </div>
                    <p className="product-price">${product.price}</p>
                    <p className="product-description">{product.description}</p>
                    {/* Features */}
                    {(product as any).features && (product as any).features.length > 0 && (
                      <div className="product-features">
                        {(product as any).features.slice(0, 4).map((feat: string) => (
                          <span key={feat} className="feature-tag">{feat}</span>
                        ))}
                      </div>
                    )}
                    <button className="buy-btn">View Details</button>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state">
              <p>No products found matching your criteria. Try a different search.</p>
              <button onClick={handleReset} className="reset-btn">View all products</button>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
