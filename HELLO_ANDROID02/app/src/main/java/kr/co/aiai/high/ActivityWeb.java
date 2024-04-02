package kr.co.aiai.high;

import androidx.appcompat.app.AppCompatActivity;

import android.content.res.AssetManager;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.IOException;
import java.io.InputStream;

public class ActivityWeb extends AppCompatActivity {

    EditText et;
    WebView wv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        et = findViewById(R.id.et_text);
        Button btn = findViewById(R.id.btn);
        Button btn2 = findViewById(R.id.btn2);
        wv = findViewById(R.id.wv);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                WebSettings settings = wv.getSettings();
                wv.setWebViewClient(new WebViewClient());
                String url = et.getText().toString().trim();
                wv.loadUrl(url);
            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                AssetManager am = getResources().getAssets() ;
                WebSettings settings = wv.getSettings();
                wv.setWebViewClient(new WebViewClient());
                String webUrlLocal = "file:///android_asset/aaaa.html";
                wv.loadUrl(webUrlLocal);
            }
        });
    }
}