/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

export default nextConfig

import { join } from 'path'

export const sassOptions = {
  includePaths: [join(__dirname, 'styles')],
}