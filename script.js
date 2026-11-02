/* ============================================================
   EKTA SINGH – Professional Developer Portfolio
   JavaScript file: script.js
   Uses: Vanilla JS + jQuery 3.7.1
   Note: No scroll-triggered reveal animations.
         All content is immediately visible on page load.
   ============================================================ */

/* ─────────────────────────────────────────────────────────
   SECTION 1 – VANILLA JAVASCRIPT
   ───────────────────────────────────────────────────────── */

/* 1.1 ── Mobile navigation toggle ─────────────────────── */
(function () {
  "use strict";

  var navToggle = document.getElementById("nav-toggle");
  var navLinks  = document.getElementById("nav-links");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      navLinks.classList.toggle("is-open");
      var isOpen = navLinks.classList.contains("is-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");

      var bars = navToggle.querySelectorAll("span");
      if (bars.length === 3) {
        if (isOpen) {
          bars[0].style.transform = "translateY(7px) rotate(45deg)";
          bars[1].style.opacity   = "0";
          bars[2].style.transform = "translateY(-7px) rotate(-45deg)";
        } else {
          bars[0].style.transform = "";
          bars[1].style.opacity   = "";
          bars[2].style.transform = "";
        }
      }
    });

    /* Close nav when clicking a link on mobile */
    var links = navLinks.querySelectorAll("a");
    links.forEach(function (link) {
      link.addEventListener("click", function () {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        var bars = navToggle.querySelectorAll("span");
        if (bars.length === 3) {
          bars[0].style.transform = "";
          bars[1].style.opacity   = "";
          bars[2].style.transform = "";
        }
      });
    });
  }
})();


/* 1.2 ── Back-to-top button visibility and smooth scroll ─ */
(function () {
  "use strict";

  var backBtn = document.getElementById("back-to-top");
  if (!backBtn) { return; }

  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 350) {
      backBtn.style.display = "flex";
      backBtn.style.opacity = "1";
    } else {
      backBtn.style.opacity = "0";
      setTimeout(function () {
        if (window.pageYOffset <= 350) {
          backBtn.style.display = "none";
        }
      }, 250);
    }
  });

  backBtn.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
})();


/* 1.3 ── Dynamic copyright year in footer ──────────────── */
(function () {
  "use strict";

  var yearSpan = document.getElementById("footer-year");
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
})();


/* 1.4 ── Smooth scrolling for internal anchor links ────── */
(function () {
  "use strict";

  var anchors = document.querySelectorAll('a[href^="#"]');
  anchors.forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      var targetId = this.getAttribute("href");
      if (targetId && targetId !== "#") {
        var targetEl = document.querySelector(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });
})();


/* 1.5 ── Highlight active nav link by current filename ─── */
(function () {
  "use strict";

  var path = window.location.pathname;
  var filename = path.substring(path.lastIndexOf("/") + 1) || "index.html";

  var navLinks = document.querySelectorAll(".site-nav__links a");
  navLinks.forEach(function (link) {
    var href = link.getAttribute("href");
    if (href === filename || (filename === "" && href === "index.html")) {
      link.classList.add("active");
    }
  });
})();


/* 1.6 ── Copy Email to Clipboard Interaction ──────────── */
(function () {
  "use strict";

  var copyBtn = document.getElementById("copy-email-trigger");
  var copyLabel = document.getElementById("copy-btn-label");
  var targetEmail = document.getElementById("target-email");

  if (copyBtn && targetEmail) {
    copyBtn.addEventListener("click", function () {
      var email = targetEmail.textContent.trim();

      function showCopied() {
        if (copyLabel) { copyLabel.textContent = "Copied!"; }
        copyBtn.classList.add("copied");
        setTimeout(function () {
          if (copyLabel) { copyLabel.textContent = "Copy"; }
          copyBtn.classList.remove("copied");
        }, 2000);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(showCopied).catch(function () {
          fallbackCopy(email);
        });
      } else {
        fallbackCopy(email);
      }

      function fallbackCopy(text) {
        var textArea = document.createElement("textarea");
        textArea.value = text;
        textArea.style.position = "fixed";
        textArea.style.left = "-9999px";
        textArea.style.top = "0";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
          document.execCommand("copy");
          showCopied();
        } catch (err) {
          if (copyLabel) { copyLabel.textContent = "Error"; }
        }
        document.body.removeChild(textArea);
      }
    });
  }
})();


/* ─────────────────────────────────────────────────────────
   SECTION 2 – JQUERY INTERACTIONS
   ───────────────────────────────────────────────────────── */
$(document).ready(function () {

  /* 2.1 ── Skill tag hover pulse (jQuery .hover) ────────── */
  $(".skill-tag").hover(
    function () {
      $(this).stop(true, true).css({ "letter-spacing": "0.14em" });
    },
    function () {
      $(this).stop(true, true).css({ "letter-spacing": "" });
    }
  );


  /* 2.2 ── Academic table row highlight (jQuery .hover) ─── */
  $(".academic-table tbody tr").hover(
    function () {
      $(this).css({
        "background-color": "#EBF2FC",
        "border-left": "4px solid #6C8FE6"
      });
    },
    function () {
      $(this).css({
        "background-color": "",
        "border-left": ""
      });
    }
  );


  /* 2.3 ── Interactive hobby card & collage item highlight (jQuery click) */
  $(".hobby-card, .collage-item").on("click", function () {
    var $el = $(this);
    if ($el.hasClass("active-editorial-card")) {
      $el.removeClass("active-editorial-card");
      $el.css({ "border-color": "", "box-shadow": "" });
    } else {
      $(".hobby-card, .collage-item").removeClass("active-editorial-card").css({ "border-color": "", "box-shadow": "" });
      $el.addClass("active-editorial-card");
      $el.css({
        "border-color": "#6C8FE6",
        "box-shadow": "0 14px 34px rgba(108, 143, 230, 0.25)"
      });
    }
  });

}); /* End $(document).ready */
