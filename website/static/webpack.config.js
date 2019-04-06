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
                use: ['vue-loader']
            },
            {
                test: /\.css$/,
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