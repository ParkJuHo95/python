package kr.co.aiai.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView

class MainActivity02 : AppCompatActivity() {

    lateinit var tv:TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main02)
        val btn = findViewById<Button>(R.id.btn)
        tv = findViewById<TextView>(R.id.tv)

        btn.setOnClickListener(){
            myClick()
        }
    }

    fun myClick(){
        var a : String = tv.text as String
        var aa : Int = a.toInt()
        aa--
        tv.text = aa.toString()
    }

}