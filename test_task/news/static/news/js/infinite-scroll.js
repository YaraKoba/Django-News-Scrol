const newsContainer = document.getElementById('news-container');
const loader = document.getElementById('loader');
let isLoading = false;

function generateNewsHTML(news_data) {
    let newHTML = ``;

    for (const data of news_data) {
        newHTML +=
        `
        <div><h2>${data}</h2></div>
        `
    };

    return newHTML;
};

const fetchMoreNews = () => {
    if (isLoading) return;
    loader.style.display = 'block';
    isLoading = true;

    setTimeout(() => {
        const newNewsHTML = generateNewsHTML([1, 2, 3, 4, 6, 7]);

        newsContainer.insertAdjacentHTML('beforeend', newNewsHTML);
        loader.style.display = 'none';
        isLoading = false
    }, 1000);
};

const handleScroll = () => {
  const scrollPosition = window.innerHeight + window.scrollY;
  if (scrollPosition >= newsContainer.offsetHeight) {
    fetchMoreNews();
  }
};


window.addEventListener('scroll', handleScroll);

fetchMoreNews();