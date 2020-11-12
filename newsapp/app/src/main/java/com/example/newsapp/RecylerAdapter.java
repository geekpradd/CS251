package com.example.newsapp;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class RecylerAdapter extends RecyclerView.Adapter<RecylerAdapter.ViewHolder> {
    private List<Article> articleList = null;
    private Context context;

    public RecylerAdapter() {
    }

    public static class ViewHolder extends RecyclerView.ViewHolder{
        View view;

        public ViewHolder(@NonNull View itemview) {
            super(itemview);
            view = itemview;
        }

        public void setContent(String content) {
            TextView news = view.findViewById(R.id.news_text);
            news.setText(content);
        }
    }

    public RecylerAdapter(List<Article> a) {
        articleList = a;
    }

    @NonNull
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup, int viewType) {
        // Create a new view, which defines the UI of the list item
        View view = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.singlenews, viewGroup, false);

        return new ViewHolder(view);
    }

    // Replace the contents of a view (invoked by the layout manager)
    @Override
    public void onBindViewHolder(ViewHolder viewHolder, final int position) {

        // Get element from your dataset at this position and replace the
        // contents of the view with that element
        viewHolder.setContent(articleList.get(position).getTitle());
    }

    public void addItems(List<Article> l) {
        Log.i("data", "new news added");
        if(articleList== null){
            articleList = l;
        }
        else {
            articleList.addAll(l);
        }
        notifyItemRangeInserted(articleList.size()-l.size(), l.size());
    }
    // Return the size of your dataset (invoked by the layout manager)
    @Override
    public int getItemCount() {
//        Log.d("debug","get length");
        if(articleList == null) {
//            Log.i("debug","empty");
            return 0;
        }
        return articleList.size();
    }
}
