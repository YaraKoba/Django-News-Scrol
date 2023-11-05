import { fetchNews } from './infinite-scroll.js'

const newsContainer = document.getElementById('news-container');
const loader = document.getElementById('loader');

let api_url = 'http://127.0.0.1:8000/api/news/?page=1';
let isLoading = false;

const getMoreNews = async () => {
  if (isLoading || !api_url) return;
  isLoading = true;
  loader.style.display = 'block'
  api_url = await fetchNews(api_url, newsContainer);
  loader.style.display = 'none'
  isLoading = false;
};

const handleScroll = async () => {
  const scrollPosition = window.innerHeight + window.scrollY;
  const containerHeight = newsContainer.offsetHeight;
  if (scrollPosition >= containerHeight) {
    await getMoreNews();
  }
};

window.addEventListener('load', getMoreNews);
window.addEventListener('scroll', handleScroll);