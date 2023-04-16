const { createProxyMiddleware } = require('http-proxy-middleware');

const BACKEND_HOST = process.env.REACT_APP_BACKEND_HOST || 'localhost';
const BACKEND_PORT = process.env.BACKEND_PORT || 5000;

module.exports = function(app) {

  app.use(
    '/',
    createProxyMiddleware({
      target: target,
      changeOrigin: true,
      logLevel: 'debug'
    })
  );

  /**
  *   You can create other proxies using app.use() method.
  */
};
