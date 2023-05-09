<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">AAC</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/speaking" class="nav-link"><p>Speaking</p> <img src="/SpeakingScreen.png" alt="Speaking Screen Image" class="nav-img"/></RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink  to="/listening" class="nav-link"><p>Listening</p> <img src="/ListeningScreen.png" alt="Listening Screen Image" class="nav-img"/> </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
</script>

<style scoped>
/* Add any component specific styles here */
.nav-img{
  width: 30px;
  height: 30px;
}

.nav-link{
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

p {
  margin: 0;
  padding: 0;
  font-size: 1rem;
}
</style>
