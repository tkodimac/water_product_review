# Water Product Review

![MOCKUP](documentation/features/mockup.png)

[View the live site here.](https://water-master-769e91fb66d4.herokuapp.com/)

Water Product Review is a comprehensive web platform where users can discover, review, and discuss various water-related products. The site allows users to explore a wide range of products, from water purifiers and filters to bottled water brands and eco-friendly water containers. Users can also share their experiences, rate products, and contribute to a community-driven resource for making informed water product choices.

## UX

### Flow

Users start their journey on the homepage, where they are greeted with an overview of the platform and featured products. The site encourages users to sign up or log in to access personalized features like submitting reviews, saving favorite products, and interacting with other community members.

The **About** page, accessible from the main navigation, provides detailed information about the platform’s purpose, highlighting the importance of informed choices when it comes to water-related products. This page serves to educate users on how the platform can help them make better purchasing decisions.

A 'Product Catalog' page allows users to browse all available products, filtered by categories such as purifiers, filters, bottled water, and containers. Logged-in users can add new products, write reviews, and rate products. This page also offers advanced search and sorting options, enabling users to find products that meet specific criteria.

Users who are not logged in can still browse the site, but they are prompted to register or log in when they try to submit a review or rate a product. Upon logging in, users are directed to their personal dashboard, where they can manage their reviews, update reviews, and view a list of their favorite product reviews.

### Colour Scheme

The color scheme reflects the theme of water, using shades of blue and green to evoke a sense of freshness and cleanliness. These colors also help create a visually calming environment, which is essential for users looking to make thoughtful, informed decisions.

The color palette was generated using [coolors.co](https://coolors.co).

![Color Palette](documentation/colours.png)

### Typography

- **[Roboto](https://fonts.google.com/specimen/Roboto)** is used for headings and body text, chosen for its modern and clean design that ensures readability.
- **[Lato](https://fonts.google.com/specimen/Lato)** is used for secondary text, providing a complementary style that enhances the overall aesthetic.
- **[Font Awesome](https://fontawesome.com)** icons are integrated throughout the site for visual cues, buttons, and interactive elements.

## User Stories

### First Time Users

- As a first-time user, I want to understand the platform's purpose to decide if it meets my needs.
- As a first-time user, I want to browse water products easily to find items of interest.
- As a first-time user, I want clear instructions on how to sign up and the benefits of doing so.
- As a first-time user, I want to see popular products and user reviews to get a sense of community engagement.
- As a first-time user, I want to search for specific products or categories to quickly find relevant items.

### Returning Site Users

- As a returning user, I want to quickly log in to access my dashboard and manage my reviews.
- As a returning user, I want to submit new reviews and rate products based on my experiences.
- As a returning user, I want to see an updated list of top-rated and trending products to stay informed.
- As a returning user, I want to easily navigate the site to explore new products and read recent reviews.
- As a returning user, I want to update my profile and manage my account settings with ease.

### Admin

- As the site admin, I want to view and manage all user accounts to maintain site security and content quality.
- As the site admin, I want to review and approve user-submitted products and reviews to ensure they meet site standards.
- As the site admin, I want to monitor site activity and user engagement to identify areas for improvement.

## Wireframes

Wireframes were created for different device sizes using [Figma](https://www.figma.com/). The design evolved during the development process, with some features adjusted for better usability.

### Desktop Wireframes

<details>
<summary>Desktop Wireframes</summary>

- Home

  ![Desktop Home](documentation/wireframes/desktop-home.png)

- Product Catalog

  ![Desktop Catalog](documentation/wireframes/desktop-catalog.png)

- Product Detail

  ![Desktop Detail](documentation/wireframes/desktop-detail.png)

- User Dashboard

  ![Desktop Dashboard](documentation/wireframes/desktop-dashboard.png)

- **About Page**

  ![Desktop About](documentation/wireframes/desktop-about.png)

</details>

### Tablet Wireframes

<details>
<summary>Tablet Wireframes</summary>

- Home

  ![Tablet Home](documentation/wireframes/tablet-home.png)

- Product Catalog

  ![Tablet Catalog](documentation/wireframes/tablet-catalog.png)

- Product Detail

  ![Tablet Detail](documentation/wireframes/tablet-detail.png)

- User Dashboard

  ![Tablet Dashboard](documentation/wireframes/tablet-dashboard.png)

- **About Page**

  ![Tablet About](documentation/wireframes/tablet-about.png)

</details>

### Mobile Wireframes

<details>
<summary>Mobile Wireframes</summary>

- Home

  ![Mobile Home](documentation/wireframes/mobile-home.png)

- Product Catalog

  ![Mobile Catalog](documentation/wireframes/mobile-catalog.png)

- Product Detail

  ![Mobile Detail](documentation/wireframes/mobile-detail.png)

- User Dashboard

  ![Mobile Dashboard](documentation/wireframes/mobile-dashboard.png)

- **About Page**

  ![Mobile About](documentation/wireframes/mobile-about.png)

</details>

## Features

### Existing Features

- **Responsive Navbar**

  The navbar is designed to provide easy access to all major sections of the site, with links displayed based on the user's login status. The responsive design ensures that the navbar adapts seamlessly across desktop, tablet, and mobile devices.

  <details>
  <summary>Navbar Screenshots</summary>

  - Desktop

    ![Desktop Navbar](documentation/features/Navbar/desktop-nav.png)

  - Tablet

    ![Tablet Navbar](documentation/features/Navbar/tablet-nav.png)

  - Mobile

    ![Mobile Navbar](documentation/features/Navbar/mobile-nav.png)

  </details>

- **Homepage**

  The homepage serves as the introduction to the platform, featuring a welcoming design with a brief overview of the site’s purpose and links to key sections like the product catalog and user reviews.

  <details>
  <summary>Page Screenshots (responsive design)</summary>

  - Desktop

    ![Desktop Home](documentation/features/pages/home-desktop.png)

  - Tablet

    ![Tablet Home](documentation/features/pages/home-tablet.png)

  - Mobile

    ![Mobile Home](documentation/features/pages/home-mobile.png)

  </details>

- **Product Catalog**

  The product catalog allows users to explore all available products, with options to filter by category, sort by rating, and search for specific items. Users can click on any product to view detailed information and read reviews.

  ![Product Catalog](documentation/features/pages/catalog.png)

- **User Dashboard**

  The user dashboard provides logged-in users with a personalized space where they can manage their reviews, update account settings, and track their favorite products.

  ![User Dashboard](documentation/features/pages/dashboard.png)

- **About Page**

  The About page provides users with an overview of the platform's mission, values, and the community. It helps users understand the purpose behind the Water Product Review platform and encourages them to join the community.

  ![About Page](documentation/features/pages/about.png)

## Future Features

- **Advanced Filtering and Sorting**

  Future updates may include more advanced filtering options, such as filtering by price range, brand, or eco-friendliness.

- **Community Forum**

  A community forum could be added to allow users to discuss water-related topics, ask questions, and share tips and advice.

- **Mobile App**

  A mobile app could be developed to enhance user accessibility and provide a more streamlined experience on mobile devices.

## Technologies Used

- **HTML5** and **CSS3** for structuring and styling the web pages.
- **JavaScript** for interactive features and dynamic content.
- **Python (Flask)** for the backend framework.
- **SQLite** for the database to store user data, reviews, and product information.
- **Bootstrap** for responsive design and layout.
- **jQuery** for DOM manipulation and event handling.
- **Font Awesome** for icons.
- **Google Fonts** for typography.

## Testing

Extensive testing was conducted to ensure that the site works as intended across different devices and browsers. All interactive elements were tested for functionality, and user feedback was incorporated into final adjustments.

### Issues

- **Browser Compatibility**
  - Resolved minor layout issues on older versions of Internet Explorer.
  
- **Responsive Design**
  - Adjusted the mobile layout to ensure all content is accessible and properly formatted on small screens.

## Deployment

The site is deployed on [Heroku](https://www.heroku.com/). Instructions for deploying the project locally are as follows:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the SQLite database by running the migration scripts.
4. Start the Flask server with `python app.py`.
5. Access the site locally via `http://localhost:5000`.

## Credits

- **Images**: Product images were sourced from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/).
- **Icons**: All icons are provided by [Font Awesome](https://fontawesome.com/).
- **Color Palette**: The color scheme was created using [Coolors](https://coolors.co/).

## Acknowledgments

Special thanks to the open-source community for providing resources and inspiration for this project. 
