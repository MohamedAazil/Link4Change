document.addEventListener('DOMContentLoaded', () => {
    loadPage('register');
});

function loadPage(page) {
    fetch(`/${page}/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
            if (page === 'investors') {
                initInvestors();
            }
        });
}

function initInvestors() {
    const investors = [
        { name: 'Investor 1', interest: 'Tech Startups' },
        { name: 'Investor 2', interest: 'Green Energy' },
        { name: 'Investor 3', interest: 'Healthcare' }
    ];

    let currentInvestorIndex = 0;
    const investorCards = document.getElementById('investorCards');

    function showInvestor() {
        investorCards.innerHTML = '';
        const investor = investors[currentInvestorIndex];
        const div = document.createElement('div');
        div.innerHTML = `<h3>${investor.name}</h3><p>${investor.interest}</p>`;
        investorCards.appendChild(div);
    }

    showInvestor();

    document.getElementById('likeBtn').addEventListener('click', () => {
        alert('You liked ' + investors[currentInvestorIndex].name);
        currentInvestorIndex = (currentInvestorIndex + 1) % investors.length;
        showInvestor();
    });

    document.getElementById('dislikeBtn').addEventListener('click', () => {
        alert('You disliked ' + investors[currentInvestorIndex].name);
        currentInvestorIndex = (currentInvestorIndex + 1) % investors.length;
        showInvestor();
    });
}
