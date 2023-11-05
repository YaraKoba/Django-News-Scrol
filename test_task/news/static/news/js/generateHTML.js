export function getTagHTML(tags) {
    let tagHTML = '';
    for (const tag of tags) {
        if (tag == 'срочные') {
            tagHTML += `<span class="badge bg-danger">${tag}</span>`;
        } else if (tag == 'обычные') {
            tagHTML += `<span class="badge bg-primary">${tag}</span>`;
        } else {
            tagHTML += `<span class="badge bg-secondary">${tag}</span>`;
        }
    }
    return tagHTML;
}


export function generateNewsHTML(news_data) {
  let newHTML = '';

  for (const item of news_data) {
    newHTML += `
      <div class="card bg-light text-start mb-3">
         <div class="row g-0">
            ${item.img ? `
              <div class="col-4 col-sm-3">
                <img src="${item.img}" width="250" height="150" class="img-fluid" alt="card-horizontal-image">
              </div>` : ''}

            <div class="col-7 col-sm-8">
              <div class="card-body">
                 <div class="card-title"><a class="text-decoration-none text-dark fs-5" style="cursor: pointer;" href="/news/news/${item.id}">${item.title}</a></div>
                 <p class="card-text">Автор: ${item.user_name}</p>
                 <p class="card-text"><small class="text-muted">${item.create_at} | Теги: ${getTagHTML(item.tags)}</small></p>
              </div>
            </div>
         </div>
      </div>
    `;
  }

  return newHTML;
}