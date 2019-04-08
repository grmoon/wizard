const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    mode: 'development',
    devtool: 'source-map',
    entry: {
        'index': path.resolve('src', 'js', 'index.js')
    },
    output: {
        path: path.resolve('dist')
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                exclude: /node_modules/,
                use: ['vue-loader']
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            '@components': path.resolve('src', 'components'),
            '@js': path.resolve('src', 'js'),
            '@utils': path.resolve('src', 'js', 'utils'),
        }
    },
    plugins: [
        new VueLoaderPlugin()
    ]
}