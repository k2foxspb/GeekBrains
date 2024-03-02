'use strict';

let basketCounterEl = document.querySelector('.cartIconWrap span');
let basketTotalEl = document.querySelector('.basketTotal');
let basketTotalValueEl = document.querySelector('.basketTotalValue');
let basketEl = document.querySelector('.basket');

document.querySelector('.cartIconWrap').addEventListener('click', () => {
    basketEl.classList.toggle('hidden');
});
let basket = {};
document
    .querySelector('.featuredItems')
    .addEventListener('click',
            event => {
    if (!event.target.closest('.addToCart')) {
        return;
    }
    let featuredItemEl = event.target.closest('.featuredItem');
    let id = +featuredItemEl.dataset.id;
    let name = featuredItemEl.dataset.name;
    let price = +featuredItemEl.dataset.price;
    addToCart(id, name, price);
});

function
addToCart(id, name, price) {
    if (!(id in basket)) {
        basket[id] = {id: id, name: name, price: price, count: 0};
    }
    basket[id].count++;
    basketCounterEl.textContent = getTotalBasketCount().toString();
    basketTotalValueEl.textContent = getTotalBasketPrice().toFixed(2);
    renderProductInBasket(id);
}

function
getTotalBasketCount() {
    return Object.values(basket).reduce((acc, product) => acc + product.count, 0);
}

function
getTotalBasketPrice() {
    return Object
        .values(basket)
        .reduce((acc, product) => acc + product.price * product.count, 0);
}

function
renderProductInBasket(productId) {
    let basketRowEl = basketEl
        .querySelector(`.basketRow[data-id="${productId}"]`);
    if (!basketRowEl) {
        renderNewProductInBasket(productId);
        return;
    }
    let product = basket[productId];
    basketRowEl.querySelector('.productCount').textContent = product.count;
    basketRowEl
        .querySelector('.productTotalRow')
        .textContent = (product.price * product.count).toFixed(2);
}

function
renderNewProductInBasket(productId) {
    let productRow = `
    <div class="basketRow" data-id="${productId}">
      <div>${basket[productId].name}</div>
      <div>
        <span class="productCount">${basket[productId].count}</span> шт.
      </div>
      <div>$${basket[productId].price}</div>
      <div>
        $<span class="productTotalRow">${(basket[productId].price * basket[productId].count).toFixed(2)}</span>
      </div>
    </div>
    `;
    basketTotalEl.insertAdjacentHTML("beforebegin", productRow);
}
