import { generateNewsHTML } from './generateHTML.js';

const newsContainer = document.getElementById('news-container');
const loader = document.getElementById('loader');
let page = 1
let isLoading = false;


function isScrollPositionEnd() {
  const scrollPosition = window.innerHeight + window.scrollY;
  const containerHeight = newsContainer.offsetHeight;

  return scrollPosition >= containerHeight;
}

const fetchMoreNews = () => {
        if (isLoading || !page) return;
        loader.style.display = 'block';
        isLoading = true;

        const apiUrl = `http://127.0.0.1:8000/api/news/?page=${page}`;

        fetch(apiUrl)
        .then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error("Ошибка при выполнении запроса");
        })
        .then(newsData => {
          const results = newsData.results;
          const newNewsHTML = generateNewsHTML(results);
          newsContainer.insertAdjacentHTML('beforeend', newNewsHTML);
          console.log(newsContainer.offsetHeight, window.innerHeight)
          loader.style.display = 'none';

          if (!newsData.next) {
            page = null
          } else {
            page++;
          }

          isLoading = false;

        if (newsContainer.offsetHeight < window.innerHeight) {
            fetchMoreNews();
        }
        });
};

const handleScroll = () => {
  if (isScrollPositionEnd()) {
    fetchMoreNews();
  }
};

window.addEventListener('scroll', handleScroll);
fetchMoreNews();

