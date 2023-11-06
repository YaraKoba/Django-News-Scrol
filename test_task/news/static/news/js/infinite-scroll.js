import { generateNewsHTML } from './generateHTML.js';

export const fetchNews = async (url, container) => {
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
    if (container.offsetHeight < window.innerHeight && next_url) {
      next_url = await fetchNews(next_url, container);
    }

    return next_url;
  } catch (error) {
    console.error(error);
    return null;
  }
};


