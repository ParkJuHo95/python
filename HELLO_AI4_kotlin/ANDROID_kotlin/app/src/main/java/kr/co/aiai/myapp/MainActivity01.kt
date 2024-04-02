package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView

class MainActivity01 : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main01)
        val btn = findViewById<Button>(R.id.btn)
        val view = findViewById<TextView>(R.id.tv)

//        val btn:Button = findViewById(R.id.btn)
//        val view:TextView = findViewById(R.id.tv)

        btn.setOnClickListener(){
            myClick()
//            view.setText("Good Evening")
        }
    }
    fun myClick(){
        Log.d("abcd","ads")
    }
}