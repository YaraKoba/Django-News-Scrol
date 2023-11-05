import { fetchNews } from './infinite-scroll.js'

const newsContainer = document.getElementById('news-container');
const loader = document.getElementById('loader');
const tagInput = document.getElementById("tag-input");
const addTagButton = document.getElementById("add-tag-button");
const searchButton = document.getElementById("search-button");
const tagList = document.getElementById("tag-list");
const tagSuggestions = document.getElementById("tag-suggestions");

let api_news = 'http://127.0.0.1:8000/api/news/?page=1';
let api_teg = 'http://127.0.0.1:8000/api/news/tags';
let isLoading = false;
let allTags = []
let addedTags = []


function searchTags() {
    const query = tagInput.value.trim();
    if (query === "") {
        tagSuggestions.innerHTML = "";
        return;
    }

    tagSuggestions.innerHTML = "";
    allTags
        .filter(tag => tag.toLowerCase().includes(query.toLowerCase()) && !addedTags.includes(tag))
        .forEach(tag => {
            const suggestion = document.createElement("li");
            suggestion.textContent = tag;
            suggestion.className = "list-group-item";
            suggestion.addEventListener("click", () => {
                tagInput.value = tag;
                tagSuggestions.innerHTML = "";
            });
            tagSuggestions.appendChild(suggestion);
        });
}

addTagButton.addEventListener("click", addTag);

function addTag() {
    const tagText = tagInput.value.trim();
    if (tagText && !addedTags.includes(tagText)) {
        addedTags.push(tagText)
        const tag = document.createElement("div");
        tag.className = "tag";
        tag.innerHTML = `
            <span>${tagText}</span>
            <span class="remove-tag">✖️</span>
        `;
        tagList.appendChild(tag);

        const removeButton = tag.querySelector(".remove-tag");
        removeButton.addEventListener("click", () => {
            tagList.removeChild(tag);
            const tagIndex = addedTags.indexOf(tag.querySelector("span").textContent);
            if (tagIndex !== -1) {
                addedTags.splice(tagIndex, 1);
            }
        });
    }
    tagInput.value = "";
    tagSuggestions.innerHTML = "";
}

const getMoreNews = async () => {
  if (isLoading || !api_news) return;
  isLoading = true;
  loader.style.display = 'block'
  api_news = await fetchNews(api_news, newsContainer);
  loader.style.display = 'none'
  isLoading = false;
};

const getTags = async () => {
    try {
        const response = await fetch(api_teg);
        if (!response.ok) {
            throw new Error("Ошибка при выполнении запроса");
        }
        const data = await response.json();
        allTags = data.tags
    } catch (error) {
        console.error(error);
        return null;
    }
  };

const reloadNews = async () => {
    if (isLoading) return;
    console.log(addedTags)
    isLoading = true;
    newsContainer.innerHTML = '';
    loader.style.display = 'block'
    api_news = 'http://127.0.0.1:8000/api/news/?page=1' + `&tags=${addedTags.join(',')}`
    api_news = await fetchNews(api_news, newsContainer);
    loader.style.display = 'none'
    isLoading = false;
}

const handleScroll = async () => {
  const scrollPosition = window.innerHeight + window.scrollY;
  const containerHeight = newsContainer.offsetHeight;
  if (scrollPosition >= containerHeight) {
    await getMoreNews();
  }
};

window.addEventListener('load', getMoreNews);
window.addEventListener('load', getTags);
window.addEventListener('scroll', handleScroll);
addTagButton.addEventListener("click", addTag);
searchButton.addEventListener("click", reloadNews)
tagInput.addEventListener("input", searchTags);
