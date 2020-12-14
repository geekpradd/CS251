package com.example.newsapp;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import com.google.android.material.appbar.CollapsingToolbarLayout;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.widget.Toast;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ScrollingActivity extends AppCompatActivity {
    private static final String API_KEY = "b274cec1287e43b399ba5c1dab082d82";
    private final RecylerAdapter Radapter = new RecylerAdapter();

    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scrolling);
        RecyclerView list = findViewById(R.id.news_holder);

        CollapsingToolbarLayout toolBarLayout = (CollapsingToolbarLayout) findViewById(R.id.toolbar_layout);
        toolBarLayout.setTitle(getTitle());
        Log.i("checks",Manifest.permission.MANAGE_DOCUMENTS.toString());
        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        list.setHasFixedSize(true);
        list.setLayoutManager(linearLayoutManager);
        list.setAdapter(Radapter);
//
//        Log.i("internet", String.valueOf(isInternetAvailable()));
//        Log.i("network", String.valueOf(isNetworkAvailable(this)));
//        Log.i("checks","view loaded");
        if(ContextCompat.checkSelfPermission(this,Manifest.permission.INTERNET) == PackageManager.PERMISSION_GRANTED) {
            Log.i("checks","permission loaded");
            addData();
            list.addOnScrollListener(new RecyclerView.OnScrollListener() {
                @Override
                public void onScrollStateChanged(@NonNull RecyclerView recyclerView, int newState) {
                    super.onScrollStateChanged(recyclerView, newState);

                    if (!recyclerView.canScrollVertically(1)) {
                        Log.i("scroll", "end reached");
                        addData();
                    }
                }
            });
        }
        else if(ActivityCompat.shouldShowRequestPermissionRationale(this,Manifest.permission.INTERNET)) {
            showExplanation();
        }
        else{
            Log.i("checks", "permission asked");
            requestPermission();
            Log.i("checks", "permission rejected");
        }
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if (requestCode == 1) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                Toast.makeText(this, "Permission Granted!", Toast.LENGTH_SHORT).show();
            } else {
                Context context = getApplicationContext();
                CharSequence text = "Internet Permission Required!";
                int duration = Toast.LENGTH_SHORT;
                Log.i("checks", "Permission denied");

                Toast toast = Toast.makeText(context, text, duration);
                toast.show();
//                System.exit(1);
            }
        }
    }

    private void addData(){
        final Api APIservice = Client.getClient().create(Api.class);
        Call<News> call = APIservice.getNews("in", API_KEY);
        call.enqueue(new Callback<News>() {
            @Override
            public void onResponse(Call<News> call, Response<News> response) {
                if(response.body() != null) {
                    if (response.body().getStatus().equals("ok")) {
                        List<Article> fetchedList = response.body().getArticles();
                        if (fetchedList.size() > 0) {
                            Radapter.addItems(fetchedList);
                        }
                    }
                }
                else {
                    Toast.makeText(getBaseContext(), "Something went wrong ;(", Toast.LENGTH_SHORT).show();
                }
            }
            @Override
            public void onFailure(Call<News> call, Throwable t) {
                Toast.makeText(getBaseContext(), "Something went wrong ;(", Toast.LENGTH_SHORT).show();
                Log.e("out", t.toString());
            }
        });
    }
    private void showExplanation() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Permission Needed")
                .setMessage("Rationale")
                .setPositiveButton(android.R.string.ok, (dialog, id) -> requestPermission());
        builder.create().show();
    }

    private void requestPermission() {
        Log.i("checks", "getting permission");
        ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.INTERNET}, 1);
    }

    @Override
    public void onStop() {
        super.onStop();
        this.finish();
    }
//
//    public boolean isInternetAvailable() {
//        try {
//            InetAddress ipAddr = InetAddress.getByName("google.com");
//            //You can replace it with your name
//            return !ipAddr.equals("");
//
//        } catch (Exception e) {
//            return false;
//        }
//    }
//    public boolean isNetworkAvailable(Context context) {
//        ConnectivityManager connectivityManager = ((ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE));
//        NetworkInfo activeNetwork = connectivityManager.getActiveNetworkInfo();
//        boolean isConnected = activeNetwork != null &&
//                activeNetwork.isConnectedOrConnecting();
//        Log.i("internet type", String.valueOf(isConnected));
//        return connectivityManager.getActiveNetworkInfo() != null && connectivityManager.getActiveNetworkInfo().isConnected();
//    }
}