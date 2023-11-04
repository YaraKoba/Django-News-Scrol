export function generateNewsHTML(news_data) {
    let newHTML = ``;

       console.log(news_data)
    for (const item of news_data) {
        newHTML +=
        `
        <div class="card bg-light text-start mb-3">
           <div class="row g-0">
              ${item.img ? `
                <div class="col-4 col-sm-3">
                  <img src="${item.img}" width="250" height="150" class="img-fluid" alt="card-horizontal-image">
                </div>` : ''}

              <div class="col-7 col-sm-8">
                <div class="card-body">
                   <h5 class="card-title">${item.title}</h5>
                   <p class="card-text">Автор: ${item.user_name}</p>
                   <p class="card-text"> </p>
                   <p class="card-text"><small class="text-muted">${item.create_at} | Тег: ${item.tags}</small></p>
                </div>
              </div>
           </div>
        </div>
        `
    };

    return newHTML;
};