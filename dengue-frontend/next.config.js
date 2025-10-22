/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/dengue/:path*',
        destination: 'https://apidadosabertos.saude.gov.br/arboviroses/dengue/:path*'
      }
    ]
  }
}

module.exports = nextConfig
