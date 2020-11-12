package com.example.newsapp;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class News {
    @SerializedName("status")
    private String status;

    @SerializedName("totalResults")
    private String len;

    @SerializedName("articles")
    private List<Article> articles = null;

    public String getStatus() {
        return status;
    }

    public String getLen() {
        return len;
    }

    public void setLen(String len) {
        this.len = len;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<Article> getArticles() {
        return articles;
    }

    public void setArticles(List<Article> articles) {
        this.articles = articles;
    }
}
