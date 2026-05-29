const CACHE_NAME = 'cap-musique-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/css/style.css',
  '/manifest.json',
  '/modules/module1-organologie.html',
  '/modules/module2-solfege.html',
  '/modules/module3-chant.html',
  '/modules/module4-pratiques.html',
  '/modules/module5-annexes.html',
  '/pratique-instrumentale.html',
  '/autres-matieres.html',
  '/contacts.html',
  '/librairie.html',
  '/informations.html',
  '/conclusion.html'
];

// Installation
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('✅ Cache ouvert');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activation
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Interception des requêtes
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});