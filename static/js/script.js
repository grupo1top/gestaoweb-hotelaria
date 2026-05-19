(() => {
	const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
	const numberFormatter = new Intl.NumberFormat("pt-BR");

	const revealItems = document.querySelectorAll("[data-reveal]");
	if (revealItems.length) {
		const revealObserver = new IntersectionObserver((entries, observer) => {
			entries.forEach((entry) => {
				if (!entry.isIntersecting) {
					return;
				}

				entry.target.classList.add("is-visible");
				observer.unobserve(entry.target);
			});
		}, {
			threshold: 0.18,
			rootMargin: "0px 0px -8% 0px",
		});

		revealItems.forEach((item, index) => {
			item.style.setProperty("--reveal-delay", `${Math.min(index * 70, 280)}ms`);
			revealObserver.observe(item);
		});
	}

	const countUps = document.querySelectorAll("[data-count-up]");
	if (countUps.length) {
		const animateCount = (element) => {
			const rawTarget = Number.parseFloat(element.dataset.countUp || "0");
			const target = Number.isFinite(rawTarget) ? rawTarget : 0;
			const decimals = String(element.dataset.countUp || "").includes(".") ? 2 : 0;

			if (reducedMotion) {
				element.textContent = numberFormatter.format(Number(target.toFixed(decimals)));
				return;
			}

			const duration = 1200;
			const startTime = performance.now();

			const frame = (currentTime) => {
				const progress = Math.min((currentTime - startTime) / duration, 1);
				const eased = 1 - Math.pow(1 - progress, 3);
				const currentValue = target * eased;

				element.textContent = numberFormatter.format(
					decimals > 0 ? Number(currentValue.toFixed(decimals)) : Math.round(currentValue)
				);

				if (progress < 1) {
					requestAnimationFrame(frame);
				}
			};

			requestAnimationFrame(frame);
		};

		const countObserver = new IntersectionObserver((entries, observer) => {
			entries.forEach((entry) => {
				if (!entry.isIntersecting) {
					return;
				}

				animateCount(entry.target);
				observer.unobserve(entry.target);
			});
		}, {
			threshold: 0.4,
		});

		countUps.forEach((item) => countObserver.observe(item));
	}
})();