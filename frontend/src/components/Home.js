import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";

export default function Home() {
    return (
        <div className="home-container">
            <header className="home-header">
                <h1 className="home-title">Welcome to AI Email Generator</h1>
                <p className="home-subtitle">Generate professional emails effortlessly with AI</p>
                <div className="home-buttons">
                    <Link to="/login" className="home-button">Login</Link>
                    <Link to="/register" className="home-button">Register</Link>
                </div>
            </header>
            <section className="home-main">
                <div className="hero-section">
                    <h2>Transform Your Email Experience</h2>
                    <p>Craft perfect emails in seconds with AI-driven suggestions, templates, and personalization.</p>
                </div>
                <div className="features-container">
                    <div className="feature-card">
                        <h3>🚀 AI-Powered Writing</h3>
                        <p>Generate high-quality emails effortlessly with AI assistance.</p>
                    </div>
                    <div className="feature-card">
                        <h3>🎨 Customizable Templates</h3>
                        <p>Choose from a variety of professionally designed templates.</p>
                    </div>
                    <div className="feature-card">
                        <h3>⏳ Time-Saving</h3>
                        <p>Eliminate writer’s block and save time composing emails.</p>
                    </div>
                    <div className="feature-card">
                        <h3>🛠 Easy to Use</h3>
                        <p>Intuitive design for a seamless user experience.</p>
                    </div>
                </div>
            </section>
            <footer className="home-footer">
                <p>© 2025 AI Email Generator. All rights reserved.</p>
            </footer>
        </div>
    );
}
