import pytest
from tests.ui.user.base_case import BaseCase


class TestAddProductToCart(BaseCase):
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_user_can_add_product_to_cart(self):
        # Step 1: Open site
        is_opened = self.home_page.is_opened()
        assert is_opened, "Home page did not open"

        # Step 2: Navigate to products
        self.header.navigate_to_products()
        assert self.products_page.is_opened(), "Products page did not open"

        # Step 3: Search product
        search_term = "Tshirt"
        self.products_page.search_product(search_term)

        # Assert search results are shown
        filtered_products = self.products_page.get_products_list()
        assert filtered_products is not None, "Products list returned None"
        assert (
            len(filtered_products) > 0
        ), f"No products found for search term: {search_term}"

        # Step 4: Add to cart
        product_index_to_add = 0

        self.products_page.add_product_to_cart(product_index_to_add)

        # Step 5: Open cart via header
        self.modal.close_modal()
        self.header.navigate_to_cart()

        assert self.cart_page.is_opened(), "Cart page did not open"

        # Step 6: Validate product in cart
        assert self.cart_page.is_product_in_cart(), "Product not found in cart"
