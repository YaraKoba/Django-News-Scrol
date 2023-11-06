import { getTagHTML } from './generateHTML.js';

const titleContainer = document.getElementById("post-title");
const bodyContainer = document.getElementById("post-body");
const subtitleContainer = document.getElementById("post-subtitle");

const likeButton = document.getElementById("likeButton");
const dislikeButton = document.getElementById("dislikeButton");
const likesCount = document.getElementById("likesCount");
const dislikesCount = document.getElementById("dislikesCount");

let isLoading = false;

const csrftoken = getCookie('csrftoken');
const postId = getPostId();

function getCookie(name) {
    const cookies = document.cookie.split(';').map(cookie => cookie.trim());
    for (const cookie of cookies) {
        if (cookie.startsWith(`${name}=`)) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return null;
}

function getPostId() {
    const pathParts = window.location.pathname.split('/');
    return pathParts[pathParts.length - 2];
}

function fetchLoadPost() {
    isLoading = true;
    const url = `http://127.0.0.1:8000/api/news/${postId}`;
    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Ошибка при выполнении запроса");
            }
        })
        .then(newsData => {
            titleContainer.insertAdjacentHTML('afterend', `<h1 class="card-header masthead-heading mb-0">${newsData.title}</h1>`);
            subtitleContainer.insertAdjacentHTML('afterend', `<small class="text-muted">${newsData.create_at} | 👁‍🗨 ${newsData.views} | Теги: ${getTagHTML(newsData.tags)}</small>`);
            bodyContainer.innerText = newsData.body;
            likesCount.innerText = newsData.likes;
            dislikesCount.innerText = newsData.dislikes;
        })
        .catch(error => {
            console.error(error);
        })
        .finally(() => {
            isLoading = false;
        });
}

function fetchLikes(data) {
    isLoading = true;
    likeButton.disabled = true;
    dislikeButton.disabled = true;

    const url = `http://127.0.0.1:8000/api/news/${postId}/change-likes`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Ошибка при выполнении запроса");
            }
        })
        .then(newLikes => {
            likesCount.innerText = newLikes.likes;
            dislikesCount.innerText = newLikes.dislikes;
        })
        .catch(error => {
            console.error(error);
        })
        .finally(() => {
            isLoading = false;
            likeButton.disabled = false;
            dislikeButton.disabled = false;
        });
}


window.addEventListener('load', fetchLoadPost);

let hasLiked = false;
let hasDisliked = false;

likeButton.addEventListener("click", () => {
    if (isLoading) return;
    var data = {}
    if (!hasLiked) {
        data.likes = 'plus';
        if (hasDisliked) {
            data.dislikes = 'minus';
            hasDisliked = false;
        }
        hasLiked = true;
    } else {
        data.likes = 'minus'
        hasLiked = false;
    }
    fetchLikes(data)
});

dislikeButton.addEventListener("click", () => {
    if (isLoading) return;
    var data = {}
    if (!hasDisliked) {
        data.dislikes = 'plus';
        if (hasLiked) {
            data.likes = 'minus';
            hasLiked = false;
        }
        hasDisliked = true;
    } else {
        data.dislikes = 'minus';
        hasDisliked = false;
    }
    fetchLikes(data)
});
