// src/App.js
import React, { useState } from 'react';
import Header from './components/Header';
import PaymentForm from './components/PaymentForm';
import Footer from './components/Footer';
import SignUp from './components/SignUp';
import SignIn from './components/SignIn';

function App() {
  const [token, setToken] = useState(null);

  const handleSignUp = (token) => {
    setToken(token);
  };

  const handleSignIn = (token) => {
    setToken(token);
  };

  return (
    <div className="App">
      <Header />
      <main>
        {token ? (
          <PaymentForm />
        ) : (
          <div>
            <SignUp onSignUp={handleSignUp} />
            <SignIn onSignIn={handleSignIn} />
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
}

export default App;
