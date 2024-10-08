const LandingPage = () => {
    return (
      <div className="landing-page">
        {/* Hero Section */}
        <section className="hero">
          <div className="hero-content">
            <h1>Discover & Review Your Favorite Manga</h1>
            <p>Explore a world of Manga, rate your favorites, and share your thoughts with other manga lovers!</p>
            <button className="cta-button">Get Started</button>
          </div>
          <div className="hero-image">
            <img src="/images/hero-manga.png" alt="Manga Reading" />
          </div>
        </section>

        {/* Features Section */}
        <section className="features">
          <h2>Why Choose MangaReview?</h2>
          <div className="features-grid">
            <div className="feature-item">
              <h3>Comprehensive Reviews</h3>
              <p>Find detailed reviews on thousands of manga titles, covering genres, plot, art, and characters.</p>
            </div>
            <div className="feature-item">
              <h3>Community Driven</h3>
              <p>Share your thoughts and engage with other manga enthusiasts through community reviews and ratings.</p>
            </div>
            <div className="feature-item">
              <h3>Stay Updated</h3>
              <p>Get alerts for the latest releases, top-rated manga, and trending reviews from the community.</p>
            </div>
          </div>
        </section>

        {/* Recent Reviews Section */}
        <section className="recent-reviews">
          <h2>Recent Reviews</h2>
          <div className="reviews-grid">
            {/* These would be dynamically populated in a real-world scenario */}
            <div className="review-item">
              <h3>Naruto</h3>
              <p>"Amazing character development, especially with Naruto and Sasuke's rivalry..."</p>
              <span>Rating: 4.5/5</span>
            </div>
            <div className="review-item">
              <h3>Attack on Titan</h3>
              <p>"Gripping and intense! Every chapter keeps you on edge."</p>
              <span>Rating: 5/5</span>
            </div>
            <div className="review-item">
              <h3>One Piece</h3>
              <p>"A masterpiece of adventure. Luffy’s journey is timeless."</p>
              <span>Rating: 4.8/5</span>
            </div>
          </div>
          <button className="see-all-button">See All Reviews</button>
        </section>

        {/* Footer Section */}
        <footer className="footer">
          <p>© 2024 MangaReview. All rights reserved.</p>
          <div className="social-icons">
            <a href="#"><img src="/images/facebook-icon.png" alt="Facebook" /></a>
            <a href="#"><img src="/images/twitter-icon.png" alt="Twitter" /></a>
            <a href="#"><img src="/images/instagram-icon.png" alt="Instagram" /></a>
          </div>
        </footer>
      </div>
    );
  };

  export default LandingPage;
