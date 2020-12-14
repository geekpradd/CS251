package com.example.newsapp;
import retrofit2.http.GET;
import retrofit2.http.Query;
import retrofit2.Call;

public interface Api{
    @GET("top-headlines")
    Call<News> getNews(@Query("country") String country, @Query("apiKey") String apiKey);
}