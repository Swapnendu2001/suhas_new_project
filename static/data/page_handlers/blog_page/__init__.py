from .hero_section import get_blog_hero_section
from .more_blogs import get_more_blogs_section
from .faq_section import get_faq_section


EMPTY_BLOG_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>News Page Dev</title>
    <link rel="icon" type="image/png" href="static/icon/website_icon.png" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>
    <link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
    rel="stylesheet"
    />
    <link
    href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap"
    rel="stylesheet"
    />
    <script>
    /* Define custom fonts in Tailwind (optional, better in tailwind.config.js) */
    tailwind.config = {
        theme: {
        extend: {
            fontFamily: {
            jakarta: ['"Plus Jakarta Sans"', "sans-serif"],
            "helvetica-now": ['"Helvetica Now Display"', "sans-serif"],
            helvetica: ['"Helvetica"', "sans-serif"],
            "ibm-plex": ['"IBM Plex Sans"', "sans-serif"],
            inter: ['"Inter"', "sans-serif"],
            },
            backgroundImage: {
            "header-banner":
                "url('digital-marketing-agency-website-banner-ad-template-lzytv.png')",
            "hero-gradient":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://picsum.photos/1920/1080')", // Placeholder image used for gradient bg
            "podcast-bg":
                "linear-gradient(360deg, rgba(255, 255, 255, 0) 74.02%, #FFFFFF 100%), linear-gradient(180deg, rgba(255, 255, 255, 0) 61.61%, #FFFFFF 100%), url('Your paragraph text (8).png')",
            "cta-bg":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.69), rgba(0, 0, 0, 0.69)), url('Screenshot 2024-09-18 at 9.57.41\u202FPM.png')",
            "gradient-line":
                "linear-gradient(90deg, #000000 0%, #9747FF 100%)",
            },
        },
        },
    };
    </script>
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        const mobileMenuButton = document.getElementById("mobile-menu-button");
        const mobileMenu = document.getElementById("mobile-menu");
        mobileMenuButton.addEventListener("click", function () {
        mobileMenu.classList.toggle("hidden");
        mobileMenuButton.classList.toggle("hamburger-active");
        if (!mobileMenu.classList.contains("hidden")) {
            mobileMenu.classList.add("slide-down");
        } else {
            mobileMenu.classList.remove("slide-down");
        }
        });
    });
    </script>
    <style>
    @media screen and (max-width: 768px) {
        .hero-text {
        font-size: 28px !important; 
        line-height: 36px !important;
        }
        .article-container {
        padding-left: 20px !important;
        padding-right: 20px !important;
        }
        .toc-container {
        padding: 10px !important;
        }
    }
    @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap");
    @font-face {
        font-family: "Helvetica Now Display";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 700;
    }
    @font-face {
        font-family: "Helvetica";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 400;
    }
    ::-webkit-scrollbar {
        display: none;
    }
    body {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }
    @keyframes slideDown {
        from {
        transform: translateY(-10px);
        opacity: 0;
        }
        to {
        transform: translateY(0);
        opacity: 1;
        }
    }
    .slide-down {
        animation: slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    :root {
        --clr-dark-black: #121212;
        --clr-bdr-gray: #2a2a2a;
        --clr-white: #fff;
        --clr-primary: #9747ff;
        --clr-primary-light: #cda7ff;
        --clr-gray-800: #1e1e1e;
    }
    .mobile-menu-item {
        padding: 0.875rem 1rem;
        background: var(--clr-dark-black);
        border-bottom: solid 1px var(--clr-bdr-gray);
        color: var(--clr-white);
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s ease;
    }
    .mobile-menu-item:hover {
        background-color: #1a1a1a;
    }
    .mobile-menu-item:active {
        background-color: #252525;
    }
    .item-title {
        flex-grow: 1;
        margin-left: 0.75rem;
        font-weight: 500;
    }
    .hamburger-line {
        transition: all 0.3s ease;
    }
    .hamburger-active .hamburger-line:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
    }
    .hamburger-active .hamburger-line:nth-child(2) {
        opacity: 0;
    }
    .hamburger-active .hamburger-line:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
    }
    .search-input {
        transition: all 0.2s ease;
    }
    .search-input:focus {
        box-shadow: 0 0 0 2px rgba(151, 71, 255, 0.5);
    }
    @keyframes shine {
        from {
        transform: translateX(-100%);
        }
        to {
        transform: translateX(100%);
        }
    }
    .login-btn {
        transition: all 0.2s ease;
    }
    .login-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(205, 167, 255, 0.4);
    }
    /* TOC container enhancements */
    aside .p-6 {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }
    .toc-container {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }
    /* Custom scrollbar for webkit browsers */
    aside .p-6::-webkit-scrollbar,
    .toc-container::-webkit-scrollbar {
        width: 6px;
    }
    aside .p-6::-webkit-scrollbar-track,
    .toc-container::-webkit-scrollbar-track {
        background: #f5f5f5;
        border-radius: 10px;
    }
    aside .p-6::-webkit-scrollbar-thumb,
    .toc-container::-webkit-scrollbar-thumb {
        background: rgba(53, 51, 205, 0.5);
        border-radius: 10px;
    }
    /* Smooth transitions for TOC links */
    .toc-link {
        transition: color 0.3s ease, font-weight 0.2s ease,
        border-color 0.3s ease;
    }
    /* Active indicator animation */
    .toc-link.text-\[\#3533CD\] {
        position: relative;
    }
    .toc-link.text-\[\#3533CD\]::after {
        content: "";
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 70%;
        background-color: #3533cd;
        border-radius: 2px;
        animation: fadeIn 0.3s ease;
    }      @keyframes fadeIn {
        from {
        opacity: 0;
        }
        to {
        opacity: 1;
        }
    }      /* Mobile TOC arrow styling for better touch targets */
    @media screen and (max-width: 1023px) {
        .toc-arrow {
        padding: 8px;
        margin: -8px;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.2s ease;
        position: relative;
        z-index: 10;
        }
        .toc-arrow:hover {
        background-color: rgba(53, 51, 205, 0.1);
        }
    }
    </style>
</head>
<body class="font-poppins bg-white text-gray-800">
    
    [[body_with_toc]]

    
    <script>
      const stripSection = document.querySelector(".strip-section");
      if (stripSection) {
        const stripContent = stripSection.querySelector(".animate-marquee");
        if (stripContent && stripContent.children.length > 0) {
          const contentWidth = stripContent.scrollWidth / 2;
          const containerWidth = stripSection.offsetWidth;
          stripContent.innerHTML += stripContent.innerHTML;
        }
      }
      // Enhanced TOC with auto-scrolling functionality
      document.addEventListener("DOMContentLoaded", function () {
        const tocDesktop = document.querySelector("aside .p-6");
        const tocMobile = document.querySelector(".toc-container");
        const tocLinks = document.querySelectorAll(".toc-link");
        const sections = document.querySelectorAll("h2[id], h3[id], p[id]");
        // Colors and styles for active/inactive states
        const activeColorClass = "text-[blue]";
        const inactiveColorClass = "text-gray-800";
        const activeFontWeightClass = "font-bold";
        const inactiveFontWeightClass = "font-medium";
        const activeBorderClass = "border-[#3533CD]";
        const inactiveBorderClass = "border-gray-200";        // Collapsible TOC functionality - different behavior for mobile and desktop
        const tocToggleLinks = document.querySelectorAll(
          "a[data-toggle-target]"
        );
        tocToggleLinks.forEach((link) => {
          const arrowIcon = link.querySelector(".toc-arrow");
          const textDiv = link.querySelector("div");
          // Handle arrow clicks for mobile
          if (arrowIcon) {
            arrowIcon.addEventListener("click", function (event) {
              event.preventDefault();
              event.stopPropagation();
              const targetId = link.getAttribute("data-toggle-target");
              const targetElement = document.querySelector(targetId);
              if (targetElement) {
                targetElement.classList.toggle("hidden");
                arrowIcon.classList.toggle("rotate-180");
              }
            });
          }
          // Handle text clicks for navigation
          if (textDiv) {
            textDiv.addEventListener("click", function (event) {
              const href = link.getAttribute("href");
              if (href && href.startsWith("#")) {
                event.preventDefault();
                const targetElement = document.querySelector(href);
                if (targetElement) {
                  targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
              }
            });
          }
          // For desktop, maintain original behavior
          link.addEventListener("click", function (event) {
            const isMobile = window.innerWidth < 1024;
            if (!isMobile) {
              const targetId = this.getAttribute("data-toggle-target");
              const targetElement = document.querySelector(targetId);
              if (targetElement) {
                targetElement.classList.toggle("hidden");
                if (arrowIcon) {
                  arrowIcon.classList.toggle("rotate-180");
                }
              }
            }
          });
        });
        // Handle sub-category links (those without data-toggle-target)
        const subCategoryLinks = document.querySelectorAll('.toc-link:not([data-toggle-target])');
        subCategoryLinks.forEach((link) => {
          link.addEventListener("click", function (event) {
            const href = this.getAttribute("href");
            if (href && href.startsWith("#")) {
              event.preventDefault();
              const targetElement = document.querySelector(href);
              if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
              }
            }
          });
        });
        // Enhanced scrollspy with TOC auto-scrolling
        function activateTocLink() {
          let currentSectionId = "";
          let currentParentSectionId = "";
          const scrollPosition = window.scrollY;
          const offset = 150; // Adjust based on header height
          let activeLink = null;
          // Find current section in view
          sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            if (scrollPosition >= sectionTop - offset) {
              currentSectionId = section.getAttribute("id");
              // Determine parent H2 section
              let parentH2 = null;
              if (section.tagName === "H2") {
                parentH2 = section;
              } else {
                // Find preceding H2
                let previousElement = section.previousElementSibling;
                while (previousElement) {
                  if (
                    previousElement.tagName === "H2" &&
                    previousElement.hasAttribute("id")
                  ) {
                    parentH2 = previousElement;
                    break;
                  }
                  previousElement = previousElement.previousElementSibling;
                }
                if (!parentH2) {
                  const parentDiv = section.closest("div");
                  if (parentDiv) {
                    const h2InDiv = parentDiv.querySelector("h2[id]");
                    if (h2InDiv) parentH2 = h2InDiv;
                  }
                }
              }
              if (parentH2) {
                currentParentSectionId = parentH2.getAttribute("id");
              } else if (section.tagName === "H2") {
                currentParentSectionId = currentSectionId;
              }
            }
          });
          // Update TOC link styles and expand sections
          tocLinks.forEach((link) => {
            const linkHref = link.getAttribute("href");
            const linkTargetId = linkHref ? linkHref.substring(1) : null;
            const isH2Link = link.classList.contains("toc-h2-link");
            const parentTocSection = link.closest(".toc-section");
            const parentSectionDataId = parentTocSection
              ? parentTocSection.dataset.sectionId
              : null;
            // Reset styles
            link.classList.remove(activeFontWeightClass);
            link.classList.add(inactiveFontWeightClass);
            link.classList.replace(activeColorClass, inactiveColorClass);
            // Border classes for subcategory links
            if (!isH2Link) {
              link.classList.replace(activeBorderClass, inactiveBorderClass);
            }
            // Highlight active link
            if (linkTargetId === currentSectionId) {
              link.classList.add(activeFontWeightClass);
              link.classList.remove(inactiveFontWeightClass);
              link.classList.replace(inactiveColorClass, activeColorClass);
              if (!isH2Link) {
                link.classList.replace(inactiveBorderClass, activeBorderClass);
              }
              activeLink = link; // Store active link for scrolling
            }
            // Highlight parent H2 if child is active
            else if (
              isH2Link &&
              parentSectionDataId === currentParentSectionId
            ) {
              link.classList.add(activeFontWeightClass);
              link.classList.remove(inactiveFontWeightClass);
            }
          });          // Auto-expand/collapse TOC sections - disabled for mobile
          document.querySelectorAll(".toc-section").forEach((tocSection) => {
            const sectionId = tocSection.dataset.sectionId;
            const subcategoriesDiv =
              tocSection.querySelector(".toc-subcategories");
            const arrowIcon = tocSection.querySelector(".toc-arrow");
            const isMobile = window.innerWidth < 1024;
            if (subcategoriesDiv && arrowIcon && !isMobile) {
              // Only auto-expand/collapse for desktop
              if (sectionId === currentParentSectionId) {
                // Expand current section
                subcategoriesDiv.classList.remove("hidden");
                arrowIcon.classList.add("rotate-180");
              } else {
                // Collapse other sections
                subcategoriesDiv.classList.add("hidden");
                arrowIcon.classList.remove("rotate-180");
              }
            }
          });
          // Scroll active link into view (for both mobile and desktop TOC)
          if (activeLink) {
            // Handle desktop TOC scrolling
            if (tocDesktop && window.innerWidth >= 1024) {
              const linkTop = activeLink.offsetTop;
              const tocTop = tocDesktop.scrollTop;
              const tocHeight = tocDesktop.clientHeight;
              // Check if link is not visible in the current view
              if (linkTop < tocTop || linkTop > tocTop + tocHeight - 50) {
                // Smoothly scroll to the active link
                tocDesktop.scrollTo({
                  top: linkTop - tocHeight / 3,
                  behavior: "smooth",
                });
              }
            }
            // Handle mobile TOC scrolling
            if (tocMobile && window.innerWidth < 1024) {
              const linkTop = activeLink.offsetTop;
              const tocTop = tocMobile.scrollTop;
              const tocHeight = tocMobile.clientHeight;
              if (linkTop < tocTop || linkTop > tocTop + tocHeight - 40) {
                tocMobile.scrollTo({
                  top: linkTop - tocHeight / 3,
                  behavior: "smooth",
                });
              }
            }
          }
        }
        // Initialize active state on load
        activateTocLink();
        // Update on scroll
        window.addEventListener("scroll", activateTocLink);
      });
    </script>
  </body>
</html>"""