import { generateNewsHTML } from './generateHTML.js';

const newsContainer = document.getElementById('news-container');
const loader = document.getElementById('loader');

const fetchNews = async (url, container) => {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error("Ошибка при выполнении запроса");
    }

    const newsData = await response.json();
    const results = newsData.results;
    const newNewsHTML = generateNewsHTML(results);
    container.insertAdjacentHTML('beforeend', newNewsHTML);
    loader.style.display = 'none';
    let next_url = newsData.next;

    if (newsContainer.offsetHeight < window.innerHeight && next_url) {
      await fetchNews(next_url, container);
    }

    return next_url;
  } catch (error) {
    console.error(error);
    return null; // или другое значение по умолчанию, если произошла ошибка
  }
};

let api_url = 'http://127.0.0.1:8000/api/news/?page=1';
let load = false;

const getMoreNews = async () => {
  if (load || !api_url) return;
  load = true;
  api_url = await fetchNews(api_url, newsContainer);
  load = false;
};

const handleScroll = () => {
  const scrollPosition = window.innerHeight + window.scrollY;
  const containerHeight = newsContainer.offsetHeight;
  if (scrollPosition >= containerHeight) {
    getMoreNews();
  }
};

window.addEventListener('load', getMoreNews);
window.addEventListener('scroll', handleScroll);
