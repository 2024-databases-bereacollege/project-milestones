<template>
  <div class="homepage">
    <header>
      <h1>UP Initiative Database</h1>
    </header>

    <main>
      <section class="hero">
        <h1></h1>
     <!--   <p>This database is a robust solution that can streamline the <br>
          storage, management, and retrieval of your data, <br>
          enhancing operational efficiency and supporting informed decision-making <br>
          across your organization.
        </p> -->
        <a href="/Instructions" class="cta-button">Get Started</a>
      </section>

      <section class="features">
        <div class="feature">
          <i class="fas fa-rocket"></i>
          <h2>Fast and Efficient</h2>
          <p>Experience lightning-fast performance and seamless user experience.</p>
        </div>
        <div class="feature">
          <i class="fas fa-mobile-alt"></i>
          <h2>Responsive Design</h2>
          <p>Enjoy a fully responsive website that looks great on all devices.</p>
        </div>
        <div class="feature">
          <i class="fas fa-shield-alt"></i>
          <h2>Secure and Reliable</h2>
          <p>Your data is safe with our robust security measures and reliable infrastructure.</p>
        </div>
      </section>
    </main>

    <footer>
      <p>&copy; 2024 UP Initiative. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
}
</script>

<style scoped>
.homepage {
  font-family: Arial, sans-serif;
  color: #333;
}

header {
  background-color: #f8f8f8;
  padding: 20px;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.hero {
  text-align: center;
  padding: 100px 0;
  background-image: url('../assets/madisonCounty.jpeg');
  background-size: 40% auto;
  background-position: center;
  color: #fff;
}

.hero h1 {
  font-size: 36px;
  margin-bottom: 20px;
}

.hero p {
  font-size: 18px;
  margin-bottom: 30px;
}

.cta-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}

.features {
  display: flex;
  justify-content: space-around;
  padding: 50px 0;
}

.feature {
  text-align: center;
  max-width: 300px;
}

.feature i {
  font-size: 48px;
  margin-bottom: 20px;
  color: #333;
}

.feature h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.feature p {
  font-size: 16px;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
}
</style>
